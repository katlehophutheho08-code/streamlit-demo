def test_import_app():
    """Import the app module to ensure it doesn't raise on import."""
    import importlib.util
    import importlib.machinery
    import os

    here = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(here, '..'))
    app_path = os.path.join(project_root, 'app.py')

    spec = importlib.util.spec_from_file_location('app', app_path)
    module = importlib.util.module_from_spec(spec)
    # execute module (this will run top-level streamlit calls but should not start server)
    spec.loader.exec_module(module)

    # module should have streamlit imported as `st`
    assert hasattr(module, 'st')
