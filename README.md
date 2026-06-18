# Model Registry

MLflow-compatible model registry with versioning and deployment.

## Features
- Model versioning with lineage tracking
- Stage transitions (staging → production → archived)
- A/B traffic splitting
- Automated rollback on metric degradation

## API
```bash
registry push model:v1 --stage staging
tregistry promote model:v1 --stage production
tregistry list --stage production
```

## License
MIT
