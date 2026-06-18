class ModelRegistry:
    def __init__(self): self.models = {}
    def register(self, name, ver, artifacts, metrics=None):
        self.models.setdefault(name, {})[ver] = {"artifacts": artifacts, "metrics": metrics or {}, "stage": "staging"}
    def promote(self, name, ver, stage): self.models[name][ver]["stage"] = stage
    def get_prod(self, name):
        for v,m in sorted(self.models.get(name,{}).items(), reverse=True):
            if m["stage"]=="production": return m
