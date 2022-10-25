def variableReplace(app, docname, source):
    """
    Takes the source on rst and replaces all the needed variables declared on
    variable_replacements structure
    """
    result = source[0]
    for key in app.config.variable_replacements:
        result = result.replace(key, app.config.variable_replacements[key])
    source[0] = result


# Add the needed variables to be replaced either on code or on text on the next
# dictionary structure.
variable_replacements = {
    # This is used in install instructions, so should be a full version
    "{InstallationVersion}" : "1.1.3",
    # This should be the same as the above except with any hyphen before
    # a release candidate replaced with dot and an additional hyphen and
    # release number added
    "{GitHubDownloadVersion}" : "1.1.3-1",
    "{userdocs}" : "https://apptainer.org/docs/user/1.1",
    "{adminversion}": "1.1",
    "{userversion}": "1.1",
    "{Project}": "Apptainer",
    "{AProject}": "An Apptainer",
    "{aProject}": "an Apptainer",
    "{command}": "apptainer",
    # Version of Go to be used in install instructions
    "{GoVersion}": "1.19.1",
    "{ENVPREFIX}": "APPTAINER",
    "{orgrepo}": "apptainer/apptainer",
    "{repobranch}": "1.1",
}


def setup(app):
    app.add_config_value('variable_replacements', {}, True)
    app.connect('source-read', variableReplace)
    app.add_css_file('custom.css')
