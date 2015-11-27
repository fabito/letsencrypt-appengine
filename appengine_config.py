from google.appengine.api import namespace_manager

# Called only if the current namespace is not set.
def namespace_manager_default_namespace_for_request():
    # The returned string will be used as the Google Apps domain.
    return "---letsencrypt---"