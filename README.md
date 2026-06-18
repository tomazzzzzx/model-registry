# Model Registry

MLflow-compatible model registry with versioning, stage transitions, and deployment automation.

## Features
- Model versioning with lineage tracking
- Stage transitions (staging → production → archived)
- A/B traffic splitting for model comparison
- Automated rollback on metric degradation

## API
```bash
registry push model:v1 --stage staging
registry promote model:v1 --stage production
registry list --stage production
```

## Integration
Compatible with MLflow model registry API. Drop-in replacement for mlflow.tracking.

## License: MIT
