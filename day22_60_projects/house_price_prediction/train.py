"""Entry point script for training and prediction.

Usage examples:
  python train.py train
  python train.py predict

This script wires together the package components and provides a simple CLI.
"""

import argparse
import json
import logging
import os
import sys

from src.house_price_prediction.data import load_california_housing, train_test_split_data
from src.house_price_prediction.features import add_engineered_features
from src.house_price_prediction.modeling import (build_model_pipelines, cross_val_rmse,
                                                evaluate, save_model_and_metrics)
from src.house_price_prediction.predict import interactive_predict, batch_predict_csv


LOG = logging.getLogger(__name__)


def configure_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')


def train(output_dir: str = None):
    X, y = load_california_housing()
    X = add_engineered_features(X)
    X_train, X_test, y_train, y_test = train_test_split_data(X, y)

    pipelines = build_model_pipelines()
    results = []
    best = None

    for name, pipe in pipelines.items():
        LOG.info('Training model: %s', name)
        pipe.fit(X_train, y_train)
        metrics = evaluate(pipe, X_test, y_test)
        metrics['cv_rmse'] = cross_val_rmse(pipe, X_train, y_train)
        metrics['model'] = name
        LOG.info('Metrics for %s: %s', name, json.dumps(metrics))
        results.append((name, pipe, metrics))

    # select best by cv_rmse
    best = min(results, key=lambda r: r[2]['cv_rmse'])
    best_name, best_model, best_metrics = best[0], best[1], best[2]
    out_dir = output_dir or os.path.join(os.getcwd(), 'models')
    model_path, metrics_path = save_model_and_metrics(best_model, best_metrics, output_dir=out_dir)
    LOG.info('Best model saved: %s', model_path)
    LOG.info('Metrics saved: %s', metrics_path)


def predict(model_path: str = None):
    X, y = load_california_housing()
    X = add_engineered_features(X)
    feature_names = list(X.columns)
    model_path = model_path or os.path.join(os.getcwd(), 'models', 'best_model.joblib')
    if not os.path.exists(model_path):
        LOG.error('Model not found at %s — run training first', model_path)
        sys.exit(1)
    interactive_predict(model_path, feature_names)


def parse_args():
    parser = argparse.ArgumentParser(description='House Price Prediction CLI')
    parser.add_argument('command', choices=['train', 'predict', 'batch-predict'], help='Command to run')
    parser.add_argument('--model-path', type=str, help='Path to model for prediction')
    parser.add_argument('--csv', type=str, help='CSV file for batch-predict')
    parser.add_argument('--output-dir', type=str, help='Output directory for model and metrics')
    return parser.parse_args()


def main():
    configure_logging()
    args = parse_args()
    if args.command == 'train':
        train(output_dir=args.output_dir)
    elif args.command == 'predict':
        predict(model_path=args.model_path)
    elif args.command == 'batch-predict':
        if not args.csv:
            LOG.error('CSV path required for batch-predict')
            sys.exit(1)
        mp = args.model_path or os.path.join(os.getcwd(), 'models', 'best_model.joblib')
        batch_predict_csv(mp, args.csv)


if __name__ == '__main__':
    main()
