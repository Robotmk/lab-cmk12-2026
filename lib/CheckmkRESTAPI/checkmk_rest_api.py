# pyright: reportArgumentType=false
from typing import Any, Iterable

from requests import Response
from robot.api.deco import keyword, library
from robot.libraries.BuiltIn import BuiltIn

from OpenApiLibCore import UNSET, OpenApiLibCore, RequestValues
from OpenApiLibCore.annotations import JSON
from OpenApiLibCore.keyword_logic.path_functions import substitute_path_parameters

run_keyword = BuiltIn().run_keyword


@library(scope="SUITE", doc_format="ROBOT")
class CheckmkRESTAPI(OpenApiLibCore):
    """Generated library with keywords for all the path operations."""

    @keyword
    def remove_acknowledgement_on_host_or_service_problems(self, body: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/acknowledge/actions/delete/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def set_acknowledgement_on_related_hosts(self, body: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/acknowledge/collections/host", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def set_acknowledgement_on_related_services(self, body: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/acknowledge/collections/service", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_pending_changes(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/activation_run/collections/pending_changes", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_currently_running_activations(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/activation_run/collections/running", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_the_activation_status(self, activation_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/activation_run/{activation_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def wait_for_activation_completion(self, activation_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/activation_run/{activation_id}/actions/wait-for-completion/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def activate_pending_changes(self, redirect: bool = UNSET, sites: list[str] = UNSET, force_foreign_changes: bool = UNSET, If_Match: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/activation_run/actions/activate-changes/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_the_status_of_the_automatic_deployment_system(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/agent/actions/automatic-deployment/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_the_baking_status(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/agent/actions/baking_status/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def download_agents_shipped_with_checkmk(self, os_type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/agent/actions/download/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def download_an_agent_by_agent_hash_and_operating_system(self, agent_hash: str = UNSET, os_type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/agent/actions/download_by_hash/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def download_an_agent_by_host_or_folder_name_and_operating_system(self, agent_type: str = UNSET, host_name: str = UNSET, folder_name: str = UNSET, os_type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/agent/actions/download_by_host/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_agents(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/agent/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_configuration_of_a_single_agent(self, agent_hash: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/agent/{agent_hash}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def bake_all_agents(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/agent/actions/bake/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def bake_and_sign_all_agents(self, key_id: str = UNSET, passphrase: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/agent/actions/bake_and_sign/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def sign_all_agents(self, key_id: str = UNSET, passphrase: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/agent/actions/sign/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def get_all_audit_log_entries(self, object_type: str = UNSET, object_id: str = UNSET, user_id: str = UNSET, date: str = UNSET, regexp: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/audit_log/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def move_audit_log_entries_to_archive(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/audit_log/actions/archive/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def call_the_autocompleter_specified_in_the_url(self, autocomplete_id: str = UNSET, value: str = UNSET, parameters: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/autocomplete/{autocomplete_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_auxiliary_tags(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/aux_tag/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

#     @keyword
#     def create_an_auxiliary_tag(self, aux_tag_id:  = UNSET, topic: str = UNSET, title: str = UNSET, help: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
#         overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
#         _ = overrides.pop("validate_against_schema", None)
#         omit_list = overrides.pop("omit_parameters", [])
#         body_data = overrides.pop("body", {})
#         overrides.update(body_data)
#         updated_path: str = substitute_path_parameters(path="/domain-types/aux_tag/collections/all", substitution_dict=overrides)
#         request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
#         request_values.remove_parameters(parameters=omit_list)
#         response = self._perform_request(request_values=request_values)
#         if validate_against_schema:
#             run_keyword('validate_response_using_validator', response)
#         return response

#     @keyword
#     def show_an_auxiliary_tag(self, aux_tag_id:  = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
#         overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
#         _ = overrides.pop("validate_against_schema", None)
#         omit_list = overrides.pop("omit_parameters", [])
#         body_data = overrides.pop("body", {})
#         overrides.update(body_data)
#         updated_path: str = substitute_path_parameters(path="/objects/aux_tag/{aux_tag_id}", substitution_dict=overrides)
#         request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
#         request_values.remove_parameters(parameters=omit_list)
#         response = self._perform_request(request_values=request_values)
#         if validate_against_schema:
#             run_keyword('validate_response_using_validator', response)
#         return response

#     @keyword
#     def update_an_aux_tag(self, aux_tag_id:  = UNSET, topic: str = UNSET, title: str = UNSET, help: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
#         overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
#         _ = overrides.pop("validate_against_schema", None)
#         omit_list = overrides.pop("omit_parameters", [])
#         body_data = overrides.pop("body", {})
#         overrides.update(body_data)
#         updated_path: str = substitute_path_parameters(path="/objects/aux_tag/{aux_tag_id}", substitution_dict=overrides)
#         request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
#         request_values.remove_parameters(parameters=omit_list)
#         response = self._perform_request(request_values=request_values)
#         if validate_against_schema:
#             run_keyword('validate_response_using_validator', response)
#         return response

#     @keyword
#     def delete_an_auxiliary_tag(self, aux_tag_id:  = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
#         overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
#         _ = overrides.pop("validate_against_schema", None)
#         omit_list = overrides.pop("omit_parameters", [])
#         body_data = overrides.pop("body", {})
#         overrides.update(body_data)
#         updated_path: str = substitute_path_parameters(path="/objects/aux_tag/{aux_tag_id}/actions/delete/invoke", substitution_dict=overrides)
#         request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
#         request_values.remove_parameters(parameters=omit_list)
#         response = self._perform_request(request_values=request_values)
#         if validate_against_schema:
#             run_keyword('validate_response_using_validator', response)
#         return response

    @keyword
    def show_the_last_status_of_a_background_job(self, job_id: str = UNSET, site_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/background_job/{job_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_peer_to_peer_broker_connections(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/broker_connection/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_peer_to_peer_broker_connection(self, connection_id: str = UNSET, connection_config: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/broker_connection/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_peer_to_peer_broker_connection(self, connection_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/broker_connection/{connection_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def edit_a_peer_to_peer_broker_connection(self, connection_id: str = UNSET, connection_config: dict[str, JSON] = UNSET, If_Match: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/broker_connection/{connection_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_a_peer_to_peer_broker_connection(self, connection_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/broker_connection/{connection_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="delete", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def get_the_state_of_bi_aggregations(self, filter_names: list[str] = UNSET, filter_groups: list[str] = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/bi_aggregation/actions/aggregation_state/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def get_the_state_of_bi_aggregations(self, filter_names: list[str] = UNSET, filter_groups: list[str] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/bi_aggregation/actions/aggregation_state/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_bi_packs(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/bi_pack/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def get_a_bi_aggregation(self, aggregation_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/bi_aggregation/{aggregation_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

#     @keyword
#     def create_a_bi_aggregation(self, aggregation_id: str = UNSET, id: str = UNSET, comment:  = UNSET, customer:  = UNSET, groups: dict[str, JSON] = UNSET, node: dict[str, JSON] = UNSET, aggregation_visualization: dict[str, JSON] = UNSET, computation_options: dict[str, JSON] = UNSET, pack_id: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
#         overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
#         _ = overrides.pop("validate_against_schema", None)
#         omit_list = overrides.pop("omit_parameters", [])
#         body_data = overrides.pop("body", {})
#         overrides.update(body_data)
#         updated_path: str = substitute_path_parameters(path="/objects/bi_aggregation/{aggregation_id}", substitution_dict=overrides)
#         request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
#         request_values.remove_parameters(parameters=omit_list)
#         response = self._perform_request(request_values=request_values)
#         if validate_against_schema:
#             run_keyword('validate_response_using_validator', response)
#         return response

#     @keyword
#     def update_an_existing_bi_aggregation(self, aggregation_id: str = UNSET, id: str = UNSET, comment:  = UNSET, customer:  = UNSET, groups: dict[str, JSON] = UNSET, node: dict[str, JSON] = UNSET, aggregation_visualization: dict[str, JSON] = UNSET, computation_options: dict[str, JSON] = UNSET, pack_id: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
#         overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
#         _ = overrides.pop("validate_against_schema", None)
#         omit_list = overrides.pop("omit_parameters", [])
#         body_data = overrides.pop("body", {})
#         overrides.update(body_data)
#         updated_path: str = substitute_path_parameters(path="/objects/bi_aggregation/{aggregation_id}", substitution_dict=overrides)
#         request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
#         request_values.remove_parameters(parameters=omit_list)
#         response = self._perform_request(request_values=request_values)
#         if validate_against_schema:
#             run_keyword('validate_response_using_validator', response)
#         return response

    @keyword
    def delete_a_bi_aggregation(self, aggregation_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/bi_aggregation/{aggregation_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="delete", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def get_a_bi_pack_and_its_rules_and_aggregations(self, pack_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/bi_pack/{pack_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_new_bi_pack(self, pack_id: str = UNSET, title: str = UNSET, contact_groups: list[str] = UNSET, public: bool = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/bi_pack/{pack_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def update_an_existing_bi_pack(self, pack_id: str = UNSET, title: str = UNSET, contact_groups: list[str] = UNSET, public: bool = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/bi_pack/{pack_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_bi_pack(self, pack_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/bi_pack/{pack_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="delete", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_bi_rule(self, rule_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/bi_rule/{rule_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_new_bi_rule(self, rule_id: str = UNSET, id: str = UNSET, nodes: list[dict[str, JSON]] = UNSET, params: dict[str, JSON] = UNSET, node_visualization: dict[str, JSON] = UNSET, properties: dict[str, JSON] = UNSET, aggregation_function: dict[str, JSON] = UNSET, computation_options: dict[str, JSON] = UNSET, pack_id: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/bi_rule/{rule_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def update_an_existing_bi_rule(self, rule_id: str = UNSET, id: str = UNSET, nodes: list[dict[str, JSON]] = UNSET, params: dict[str, JSON] = UNSET, node_visualization: dict[str, JSON] = UNSET, properties: dict[str, JSON] = UNSET, aggregation_function: dict[str, JSON] = UNSET, computation_options: dict[str, JSON] = UNSET, pack_id: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/bi_rule/{rule_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_bi_rule(self, rule_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/bi_rule/{rule_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="delete", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_agent_controller_certificate_settings(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/agent_controller_certificates_settings", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def x_509_pem_encoded_root_certificate(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/root_cert", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def x_509_pem_encoded_certificate_signing_requests_csrs(self, csr: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/csr", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_comments(self, collection_name: str = UNSET, host_name: str = UNSET, service_description: str = UNSET, site_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/comment/collections/{collection_name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_comment(self, comment_id: int = UNSET, site_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/comment/{comment_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_comments(self, body: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/comment/actions/delete/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_host_comment(self, body: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/comment/collections/host", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_service_comment(self, body: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/comment/collections/service", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def get_a_configuration_entity_form_spec_schema(self, entity_type: str = UNSET, entity_type_specifier: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/form_spec/collections/{entity_type}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def update_an_existing_configuration_entity(self, entity_type: str = UNSET, entity_type_specifier: str = UNSET, entity_id: str = UNSET, data: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/configuration_entity/actions/edit-single-entity/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_configuration_entity(self, entity_type: str = UNSET, entity_type_specifier: str = UNSET, data: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/configuration_entity/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def list_existing_folder(self, entity_type_specifier: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/folder/collections/{entity_type_specifier}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def list_existing_notification_parameters(self, entity_type_specifier: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/notification_parameter/collections/{entity_type_specifier}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def get_a_notification_parameter(self, entity_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/notification_parameter/{entity_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def list_oauth2_configuration_entities(self, entity_type_specifier: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/oauth2_connection/collections/{entity_type_specifier}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def get_an_oauth2_connection(self, entity_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/oauth2_connection/{entity_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def list_existing_passwordstore_passwords(self, entity_type_specifier: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/passwordstore_password/collections/{entity_type_specifier}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def list_existing_rules(self, entity_type_specifier: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/rule_form_spec/collections/{entity_type_specifier}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def get_a_rule_form_spec_parameter(self, entity_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/rule_form_spec/{entity_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_contact_groups(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/contact_group_config/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_contact_group(self, name: str = UNSET, alias: str = UNSET, inventory_paths: dict[str, JSON] = UNSET, customer: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/contact_group_config/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_contact_group(self, name: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/contact_group_config/{name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def update_a_contact_group(self, name: str = UNSET, alias: str = UNSET, inventory_paths: dict[str, JSON] = UNSET, customer: str = UNSET, If_Match: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/contact_group_config/{name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_a_contact_group(self, name: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/contact_group_config/{name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="delete", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def bulk_update_contact_groups(self, entries: list[dict[str, JSON]] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/contact_group_config/actions/bulk-update/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def bulk_create_contact_groups(self, entries: list[dict[str, JSON]] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/contact_group_config/actions/bulk-create/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def bulk_delete_contact_groups(self, entries: list[str] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/contact_group_config/actions/bulk-delete/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_scheduled_downtimes(self, service_description: str = UNSET, host_name: str = UNSET, downtime_type: str = UNSET, site_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/downtime/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_downtime(self, downtime_id: str = UNSET, site_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/downtime/{downtime_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def modify_a_scheduled_downtime(self, body: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/downtime/actions/modify/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_a_scheduled_downtime(self, body: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/downtime/actions/delete/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_host_related_scheduled_downtime(self, body: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/downtime/collections/host", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_service_related_scheduled_downtime(self, body: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/downtime/collections/service", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def fetch_phase_1_result(self, connection_id: str = UNSET, site_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/dcd/actions/fetch_phase_one/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_dynamic_host_configuration(self, dcd_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/dcd/{dcd_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_a_dynamic_host_configuration(self, dcd_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/dcd/{dcd_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="delete", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_dynamic_host_configuration(self, title: str = UNSET, comment: str = UNSET, documentation_url: str = UNSET, disabled: bool = UNSET, site: str = UNSET, dcd_id: str = UNSET, connector: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/dcd/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_events(self, host: str = UNSET, application: str = UNSET, state: str = UNSET, phase: str = UNSET, site_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/event_console/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_an_event(self, event_id: str = UNSET, site_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/event_console/{event_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def change_multiple_event_states(self, body: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/event_console/actions/change_state/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def archive_events(self, body: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/event_console/actions/delete/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def update_and_acknowledge_events(self, body: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/event_console/actions/update_and_acknowledge/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def change_event_state(self, event_id: str = UNSET, site_id: str = UNSET, new_state: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/event_console/{event_id}/actions/change_state/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def update_and_acknowledge_an_event(self, event_id: str = UNSET, phase: str = UNSET, change_comment: str = UNSET, change_contact: str = UNSET, site_id: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/event_console/{event_id}/actions/update_and_acknowledge/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_folders(self, parent: str = UNSET, recursive: bool = UNSET, show_hosts: bool = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/folder_config/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_folder(self, name: str = UNSET, title: str = UNSET, parent: str = UNSET, attributes: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/folder_config/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_folder(self, folder: str = UNSET, show_hosts: bool = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/folder_config/{folder}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def update_a_folder(self, folder: str = UNSET, title: str = UNSET, attributes: dict[str, JSON] = UNSET, update_attributes: dict[str, JSON] = UNSET, remove_attributes: list[str] = UNSET, If_Match: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/folder_config/{folder}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_a_folder(self, folder: str = UNSET, delete_mode: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/folder_config/{folder}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="delete", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_hosts_in_a_folder(self, folder: str = UNSET, effective_attributes: bool = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/folder_config/{folder}/collections/hosts", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def bulk_update_folders(self, entries: list[dict[str, JSON]] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/folder_config/actions/bulk-update/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def move_a_folder(self, folder: str = UNSET, destination: str = UNSET, If_Match: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/folder_config/{folder}/actions/move/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_host_groups(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/host_group_config/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_host_group(self, customer: str = UNSET, name: str = UNSET, alias: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/host_group_config/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_host_group(self, name: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/host_group_config/{name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def update_a_host_group(self, name: str = UNSET, alias: str = UNSET, customer: str = UNSET, If_Match: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/host_group_config/{name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_a_host_group(self, name: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/host_group_config/{name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="delete", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def bulk_update_host_groups(self, entries: list[dict[str, JSON]] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/host_group_config/actions/bulk-update/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def bulk_create_host_groups(self, entries: list[dict[str, JSON]] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/host_group_config/actions/bulk-create/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def bulk_delete_host_groups(self, entries: list[str] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/host_group_config/actions/bulk-delete/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_host_tag_groups(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/host_tag_group/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_host_tag_group(self, id: str = UNSET, title: str = UNSET, topic: str = UNSET, help: str = UNSET, tags: list[dict[str, JSON]] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/host_tag_group/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_host_tag_group(self, name: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/host_tag_group/{name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def update_a_host_tag_group(self, name: str = UNSET, title: str = UNSET, topic: str = UNSET, help: str = UNSET, tags: list[dict[str, JSON]] = UNSET, repair: bool = UNSET, If_Match: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/host_tag_group/{name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

#     @keyword
#     def delete_a_host_tag_group(self, name: str = UNSET, repair: bool = UNSET, mode:  = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
#         overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
#         _ = overrides.pop("validate_against_schema", None)
#         omit_list = overrides.pop("omit_parameters", [])
#         body_data = overrides.pop("body", {})
#         overrides.update(body_data)
#         updated_path: str = substitute_path_parameters(path="/objects/host_tag_group/{name}", substitution_dict=overrides)
#         request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="delete", overrides=overrides)
#         request_values.remove_parameters(parameters=omit_list)
#         response = self._perform_request(request_values=request_values)
#         if validate_against_schema:
#             run_keyword('validate_response_using_validator', response)
#         return response

    @keyword
    def wait_for_renaming_process_completion(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/host_config/actions/wait-for-completion/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_hosts(self, effective_attributes: bool = UNSET, include_links: bool = UNSET, fields: str = UNSET, hostnames: list[str] = UNSET, site: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/host_config/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_host(self, host_name: str = UNSET, folder: str = UNSET, attributes: dict[str, JSON] = UNSET, bake_agent: bool = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/host_config/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_host(self, host_name: str = UNSET, effective_attributes: bool = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/host_config/{host_name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def update_a_host(self, host_name: str = UNSET, attributes: dict[str, JSON] = UNSET, update_attributes: dict[str, JSON] = UNSET, remove_attributes: list[str] = UNSET, If_Match: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/host_config/{host_name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_a_host(self, host_name: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/host_config/{host_name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="delete", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def bulk_update_hosts(self, entries: list[dict[str, JSON]] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/host_config/actions/bulk-update/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def rename_a_host(self, host_name: str = UNSET, new_name: str = UNSET, If_Match: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/host_config/{host_name}/actions/rename/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def update_the_nodes_of_a_cluster_host(self, host_name: str = UNSET, nodes: list[str] = UNSET, If_Match: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/host_config/{host_name}/properties/nodes", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def bulk_create_hosts(self, entries: list[dict[str, JSON]] = UNSET, bake_agent: bool = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/host_config/actions/bulk-create/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def bulk_delete_hosts(self, entries: list[str] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/host_config/actions/bulk-delete/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_cluster_host(self, host_name: str = UNSET, folder: str = UNSET, attributes: dict[str, JSON] = UNSET, nodes: list[str] = UNSET, bake_agent: bool = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/host_config/collections/clusters", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def move_a_host_to_another_folder(self, host_name: str = UNSET, target_folder: str = UNSET, If_Match: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/host_config/{host_name}/actions/move/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_host(self, host_name: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/host_config_internal/{host_name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def link_a_host_to_a_uuid(self, host_name: str = UNSET, uuid: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/host_config_internal/{host_name}/actions/link_uuid/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def register_an_existing_host_ie_link_it_to_a_uuid(self, host_name: str = UNSET, uuid: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/host_config_internal/{host_name}/actions/register/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_ldap_connections(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/ldap_connection/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_an_ldap_connection(self, users: dict[str, JSON] = UNSET, groups: dict[str, JSON] = UNSET, sync_plugins: dict[str, JSON] = UNSET, other: dict[str, JSON] = UNSET, general_properties: dict[str, JSON] = UNSET, ldap_connection: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/ldap_connection/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_an_ldap_connection(self, ldap_connection_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/ldap_connection/{ldap_connection_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def update_an_ldap_connection(self, ldap_connection_id: str = UNSET, users: dict[str, JSON] = UNSET, groups: dict[str, JSON] = UNSET, sync_plugins: dict[str, JSON] = UNSET, other: dict[str, JSON] = UNSET, general_properties: dict[str, JSON] = UNSET, ldap_connection: dict[str, JSON] = UNSET, If_Match: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/ldap_connection/{ldap_connection_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_an_ldap_connection(self, ldap_connection_id: str = UNSET, If_Match: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/ldap_connection/{ldap_connection_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="delete", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def download_the_license_usage_of_checkmk(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/license_usage/actions/download/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def configure_the_licensing_settings(self, settings: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/licensing/actions/configure/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def trigger_the_offline_license_verification_and_receive_its_results(self, VERSION: str = UNSET, request_id: str = UNSET, response_id: str = UNSET, created_at: int = UNSET, signature: str = UNSET, certificate: str = UNSET, payload: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/license_response/actions/upload/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def trigger_the_license_verification_and_receive_its_results(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/licensing/actions/verify/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def get_metrics_using_filters(self, body: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/metric/actions/filter/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def get_metrics(self, body: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/metric/actions/get/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def display_some_version_information(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/version", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_notification_rules(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/notification_rule/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_notification_rule(self, rule_config: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/notification_rule/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_notification_rule(self, rule_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/notification_rule/{rule_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def update_a_notification_rule(self, rule_id: str = UNSET, rule_config: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/notification_rule/{rule_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_a_notification_rule(self, rule_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/notification_rule/{rule_id}/actions/delete/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def start_the_parent_scan_background_job(self, host_names: list[str] = UNSET, performance: dict[str, JSON] = UNSET, configuration: dict[str, JSON] = UNSET, gateway_hosts: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/parent_scan/actions/start/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_passwords(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/password/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_password(self, ident: str = UNSET, title: str = UNSET, comment: str = UNSET, documentation_url: str = UNSET, password: str = UNSET, owner: str = UNSET, editable_by: str = UNSET, shared: list[str] = UNSET, customer: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/password/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_the_metadata_of_a_password_store_entry(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/password/{name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def update_a_password(self, title: str = UNSET, comment: str = UNSET, documentation_url: str = UNSET, password: str = UNSET, owner: str = UNSET, editable_by: str = UNSET, shared: list[str] = UNSET, customer: str = UNSET, If_Match: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/password/{name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_a_password(self, If_Match: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/password/{name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="delete", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def get_guided_stages_or_overview_stages(self, quick_setup_id: str = UNSET, mode: str = UNSET, object_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/quick_setup/{quick_setup_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def get_a_quick_setup_stage_structure(self, quick_setup_id: str = UNSET, stage_index: str = UNSET, object_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/quick_setup/{quick_setup_id}/quick_setup_stage/{stage_index}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def fetch_the_quick_action_background_job_result(self, job_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/quick_setup_action_result/{job_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def fetch_the_quick_setup_stage_action_background_job_result(self, job_id: str = UNSET, site_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/quick_setup_stage_action_result/{job_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def edit_the_quick_setup(self, quick_setup_id: str = UNSET, button_id: str = UNSET, stages: list[dict[str, JSON]] = UNSET, object_id: str = UNSET, search: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/quick_setup/{quick_setup_id}/actions/edit/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def run_a_quick_setup_action(self, quick_setup_id: str = UNSET, button_id: str = UNSET, stages: list[dict[str, JSON]] = UNSET, mode: str = UNSET, search: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/quick_setup/{quick_setup_id}/actions/run-action/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def run_a_quick_setup_stage_validation_and_recap_action(self, quick_setup_id: str = UNSET, stage_action_id: str = UNSET, stages: list[dict[str, JSON]] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/quick_setup/{quick_setup_id}/actions/run-stage-action/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def list_rules(self, ruleset_name: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/rule/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_rule(self, properties: dict[str, JSON] = UNSET, value_raw: str = UNSET, conditions: dict[str, JSON] = UNSET, ruleset: str = UNSET, folder: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/rule/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_rule(self, rule_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/rule/{rule_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def modify_a_rule(self, rule_id: str = UNSET, properties: dict[str, JSON] = UNSET, value_raw: str = UNSET, conditions: dict[str, JSON] = UNSET, If_Match: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/rule/{rule_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_a_rule(self, rule_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/rule/{rule_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="delete", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def move_a_rule_to_a_specific_location(self, rule_id: str = UNSET, body: dict[str, JSON] = UNSET, If_Match: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/rule/{rule_id}/actions/move/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def search_rule_sets(self, fulltext: str = UNSET, folder: str = UNSET, deprecated: bool = UNSET, used: bool = UNSET, name: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/ruleset/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_ruleset(self, ruleset_name: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/ruleset/{ruleset_name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_saml_connections(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/saml_connection/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_saml_connection(self, general_properties: dict[str, JSON] = UNSET, connection_config: dict[str, JSON] = UNSET, security: dict[str, JSON] = UNSET, users: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/saml_connection/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_saml_connection(self, saml_connection_id: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/saml_connection/{saml_connection_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_a_saml_connection(self, saml_connection_id: str = UNSET, If_Match: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/saml_connection/{saml_connection_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="delete", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def compute_the_sla_data(self, sla_compute_targets: list[dict[str, JSON]] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/sla/actions/compute/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_the_current_service_discovery_result(self, host_name: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/service_discovery/{host_name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_the_last_service_discovery_background_job_on_a_host(self, host_name: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/service_discovery_run/{host_name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def wait_for_service_discovery_completion(self, host_name: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/service_discovery_run/{host_name}/actions/wait-for-completion/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

#     @keyword
#     def update_the_phase_of_a_service(self, host_name: str = UNSET, check_type: str = UNSET, service_item:  = UNSET, target_phase: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
#         overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
#         _ = overrides.pop("validate_against_schema", None)
#         omit_list = overrides.pop("omit_parameters", [])
#         body_data = overrides.pop("body", {})
#         overrides.update(body_data)
#         updated_path: str = substitute_path_parameters(path="/objects/host/{host_name}/actions/update_discovery_phase/invoke", substitution_dict=overrides)
#         request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
#         request_values.remove_parameters(parameters=omit_list)
#         response = self._perform_request(request_values=request_values)
#         if validate_against_schema:
#             run_keyword('validate_response_using_validator', response)
#         return response

    @keyword
    def start_a_bulk_discovery_job(self, hostnames: list[str] = UNSET, options: dict[str, JSON] = UNSET, do_full_scan: bool = UNSET, bulk_size: int = UNSET, ignore_errors: bool = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/discovery_run/actions/bulk-discovery-start/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def execute_a_service_discovery_on_a_host(self, host_name: str = UNSET, mode: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/service_discovery_run/actions/start/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_service_groups(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/service_group_config/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_service_group(self, customer: str = UNSET, name: str = UNSET, alias: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/service_group_config/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_service_group(self, name: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/service_group_config/{name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def update_a_service_group(self, name: str = UNSET, alias: str = UNSET, customer: str = UNSET, If_Match: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/service_group_config/{name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_a_service_group(self, name: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/service_group_config/{name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="delete", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def bulk_update_service_groups(self, entries: list[dict[str, JSON]] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/service_group_config/actions/bulk-update/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def bulk_create_service_groups(self, entries: list[dict[str, JSON]] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/service_group_config/actions/bulk-create/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def bulk_delete_service_groups(self, entries: list[str] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/service_group_config/actions/bulk-delete/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_single_service_of_a_specific_host(self, host_name: str = UNSET, service_description: str = UNSET, columns: list[str] = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/host/{host_name}/actions/show_service/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_monitored_services(self, sites: list[str] = UNSET, columns: list[str] = UNSET, query: dict[str, JSON] = UNSET, host_name: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/service/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_the_monitored_services_of_a_host(self, host_name: str = UNSET, sites: list[str] = UNSET, columns: list[str] = UNSET, query: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/host/{host_name}/collections/services", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_site_connections(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/site_connection/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_site_connection(self, site_config: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/site_connection/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_site_connection(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/site_connection/{site_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def edit_a_site_connection(self, site_config: dict[str, JSON] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/site_connection/{site_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_a_site_connection(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/site_connection/{site_id}/actions/delete/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def login_to_a_remote_site(self, username: str = UNSET, password: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/site_connection/{site_id}/actions/login/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def logout_from_a_remote_site(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/site_connection/{site_id}/actions/logout/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_time_periods(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/time_period/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_time_period(self, name: str = UNSET, alias: str = UNSET, active_time_ranges: list[dict[str, JSON]] = UNSET, exceptions: list[dict[str, JSON]] = UNSET, exclude: list[str] = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/time_period/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_time_period(self, name: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/time_period/{name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def update_a_time_period(self, name: str = UNSET, alias: str = UNSET, active_time_ranges: list[dict[str, JSON]] = UNSET, exceptions: list[dict[str, JSON]] = UNSET, exclude: list[str] = UNSET, If_Match: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/time_period/{name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_a_time_period(self, name: str = UNSET, If_Match: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/time_period/{name}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="delete", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_user_roles(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/user_role/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_user_role(self, role_id: str = UNSET, new_role_id: str = UNSET, new_alias: str = UNSET, enforce_two_factor_authentication: bool = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/user_role/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_user_role(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/user_role/{role_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def edit_a_user_role(self, new_role_id: str = UNSET, new_alias: str = UNSET, new_basedon: str = UNSET, new_permissions: dict[str, JSON] = UNSET, enforce_two_factor_authentication: bool = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/user_role/{role_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_a_user_role(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/user_role/{role_id}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="delete", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_all_users(self, validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/user_config/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def create_a_user(self, username: str = UNSET, fullname: str = UNSET, customer: str = UNSET, auth_option: dict[str, JSON] = UNSET, disable_login: bool = UNSET, contact_options: dict[str, JSON] = UNSET, pager_address: str = UNSET, idle_timeout: dict[str, JSON] = UNSET, roles: list[str] = UNSET, authorized_sites: list[str] = UNSET, contactgroups: list[str] = UNSET, disable_notifications: dict[str, JSON] = UNSET, language: str = UNSET, temperature_unit: str = UNSET, interface_options: dict[str, JSON] = UNSET, start_url: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/user_config/collections/all", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def show_a_user(self, username: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/user_config/{username}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="get", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def edit_a_user(self, username: str = UNSET, fullname: str = UNSET, customer: str = UNSET, auth_option: dict[str, JSON] = UNSET, disable_login: bool = UNSET, contact_options: dict[str, JSON] = UNSET, pager_address: str = UNSET, idle_timeout: dict[str, JSON] = UNSET, roles: list[str] = UNSET, authorized_sites: list[str] = UNSET, contactgroups: list[str] = UNSET, disable_notifications: dict[str, JSON] = UNSET, language: str = UNSET, temperature_unit: str = UNSET, interface_options: dict[str, JSON] = UNSET, start_url: str = UNSET, If_Match: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/user_config/{username}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="put", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def delete_a_user(self, username: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/objects/user_config/{username}", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="delete", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def save_a_warning_dismissal_for_the_current_user(self, warning: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/user_config/actions/dismiss-warning/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @keyword
    def get_a_custom_graph(self, time_range: dict[str, JSON] = UNSET, reduce: str = UNSET, custom_graph_id: str = UNSET, Content_Type: str = UNSET, omit_parameters: Iterable[str] = frozenset(), validate_against_schema: bool = True) -> Response:
        overrides = {key: value for key, value in locals().items() if value is not UNSET and key != "self"}
        _ = overrides.pop("validate_against_schema", None)
        omit_list = overrides.pop("omit_parameters", [])
        body_data = overrides.pop("body", {})
        overrides.update(body_data)
        updated_path: str = substitute_path_parameters(path="/domain-types/metric/actions/get_custom_graph/invoke", substitution_dict=overrides)
        request_values: RequestValues = self.get_request_values(path=f"{updated_path}", method="post", overrides=overrides)
        request_values.remove_parameters(parameters=omit_list)
        response = self._perform_request(request_values=request_values)
        if validate_against_schema:
            run_keyword('validate_response_using_validator', response)
        return response

    @staticmethod
    def _perform_request(request_values: RequestValues) -> Response:
        response: Response = run_keyword(
            "Authorized Request",
            request_values.url,
            request_values.method,
            request_values.params,
            request_values.headers,
            request_values.json_data,
        )
        return response