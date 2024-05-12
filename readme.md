

```powershell
uv pip install
```


```powershell
Remove-Item Env:\CONDA_PREFIX
```

```powershell
uv pip freeze | uv pip compile - -o requirements.txt
```

