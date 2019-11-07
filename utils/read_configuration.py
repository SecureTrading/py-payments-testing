"""Separate module to read framework configuration"""
# -*- coding: utf-8 -*-

import os


def get_from_env(key, default=None, project_name=None):
    if project_name:
        key = f'{project_name}_{key}'
    value = os.getenv(key, default)
    return value


def get_path_from_env(key, default=None, project_name=None):
    path = get_from_env(key, default, project_name)
    path = resolve_path(path)
    return path


def resolve_path(path_to_resolve):
    spath = path_to_resolve.replace('\\', '/')
    spath = spath.split('/')
    path_to_resolve = os.path.join(*spath)
    if not os.path.isabs(path_to_resolve):
        project_path = os.getcwd()
        path_to_resolve = os.path.normpath(os.path.join(project_path, path_to_resolve))
    return path_to_resolve
