"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'decision_1' block
    decision_1(container=container)

    return

@phantom.playbook_block()
def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("decision_1() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["artifact:*.cef.fileHash", "in", "custom_list:Prior Hashes"]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        add_comment_1(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'elif' condition 2
    found_match_2 = phantom.decision(
        container=container,
        conditions=[
            ["artifact:*.cef.fileHash", "not in", "custom_list:Prior Hashes"]
        ],
        delimiter=None)

    # call connected blocks if condition 2 matched
    if found_match_2:
        add_comment_add_to_list_2(action=action, success=success, container=container, results=results, handle=handle)
        return

    return


@phantom.playbook_block()
def add_comment_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("add_comment_1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment="Hash has been previously observed.")

    old_hash(container=container)

    return


@phantom.playbook_block()
def add_comment_add_to_list_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("add_comment_add_to_list_2() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.fileHash"])

    container_artifact_cef_item_0 = [item[0] for item in container_artifact_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment="Hash has not been previously observered.")
    phantom.add_list(list_name="Prior Hashes", values=container_artifact_cef_item_0)

    new_hash(container=container)

    return


@phantom.playbook_block()
def old_hash(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("old_hash() called")

    ################################################################################
    # This file has been observed before
    ################################################################################

    template = """This file has been observed before\n"""

    # parameter list for template variable replacement
    parameters = [
        ""
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="old_hash")

    join_concatenate_hash_status(container=container)

    return


@phantom.playbook_block()
def new_hash(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("new_hash() called")

    ################################################################################
    # This file has not been observed before
    ################################################################################

    template = """This file has not been observed before\n"""

    # parameter list for template variable replacement
    parameters = [
        ""
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="new_hash")

    join_concatenate_hash_status(container=container)

    return


@phantom.playbook_block()
def join_concatenate_hash_status(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("join_concatenate_hash_status() called")

    # call connected block "concatenate_hash_status"
    concatenate_hash_status(container=container, handle=handle)

    return


@phantom.playbook_block()
def concatenate_hash_status(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("concatenate_hash_status() called")

    template = """{0}{1}\n"""

    # parameter list for template variable replacement
    parameters = [
        "new_hash:formatted_data",
        "old_hash:formatted_data"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="concatenate_hash_status")

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    concatenate_hash_status = phantom.get_format_data(name="concatenate_hash_status")

    output = {
        "hash_status": concatenate_hash_status,
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_playbook_output_data(output=output)

    return