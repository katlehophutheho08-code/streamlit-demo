def test_increment_changes_session_state():
    """Import `app.py` by path (like other tests) and verify increment()."""
    import importlib.util
    import os

    here = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(here, '..'))
    app_path = os.path.join(project_root, 'app.py')

    spec = importlib.util.spec_from_file_location('app', app_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Ensure 'count' exists and is an integer
    assert hasattr(module, 'st')
    initial = module.st.session_state.get('count', 0)

    # Call increment and verify the session state changed
    module.increment()
    assert module.st.session_state.count == initial + 1
