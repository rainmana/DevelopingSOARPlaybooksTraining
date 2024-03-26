"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'format_2' block
    format_2(container=container)

    return

@phantom.playbook_block()
def format_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_2() called")

    template = """A file has been detected that has been determined to be potentially malicious. A case has been opened.\n\n- **Case link**: {0}\n- **Event Name**: {1}\n- **Description**: {2}\n- **Source URL**: {3}\n- **Target Server IP**: {4}\n- **Suspicious File Path**: {5} \n- **Reason for promotion**: {6}"""

    # parameter list for template variable replacement
    parameters = [
        "container:url",
        "container:name",
        "container:description",
        "artifact:*.cef.sourceDnsDomain",
        "artifact:*.cef.destinationAddress",
        "artifact:*.cef.filePath",
        "playbook_input:promotion_reason"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_2", drop_none=True)

    promote_to_case_add_comment_add_note_2(container=container)

    return


@phantom.playbook_block()
def promote_to_case_add_comment_add_note_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("promote_to_case_add_comment_add_note_2() called")

    format_2__as_list = phantom.get_format_data(name="format_2__as_list")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.promote(container=container, template="Data Breach")
    phantom.comment(container=container, comment="Promoted to Case")
    phantom.add_note(container=container, content=format_2__as_list, note_format="markdown", note_type="general", title="Incident Report")

    container = phantom.get_container(container.get('id', None))

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    return