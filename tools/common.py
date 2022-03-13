import yaml


def _get_from_config(key, configpath='./mkdocs.yml'):
    yaml.add_multi_constructor('tag:yaml.org,2002:python/name', lambda loader, suffix, node: None, Loader=yaml.SafeLoader)

    with open(configpath, 'r') as f:
        config = yaml.safe_load(f)
    
    return config.get(key)


def site_url(configpath='./mkdocs.yml'):
    return _get_from_config('site_url', configpath=configpath)


def repo_url(configpath='./mkdocs.yml'):
    return _get_from_config('repo_url', configpath=configpath)