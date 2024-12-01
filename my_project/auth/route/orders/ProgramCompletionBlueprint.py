from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import program_completion_controller
from my_project.auth.domain.orders.ProgramCompletion import ProgramCompletion

program_completion_bp = Blueprint('program_completion', __name__, url_prefix='/program_completion')

@program_completion_bp.get('')
def get_all_program_completions() -> Response:
    completions = program_completion_controller.find_all()
    completions_dto = [completion.put_into_dto() for completion in completions]
    return make_response(jsonify(completions_dto), HTTPStatus.OK)

@program_completion_bp.post('')
def create_program_completion() -> Response:
    content = request.get_json()
    completion = ProgramCompletion.create_from_dto(content)
    program_completion_controller.create(completion)
    return make_response(jsonify(completion.put_into_dto()), HTTPStatus.CREATED)

@program_completion_bp.get('/<int:completion_id>')
def get_program_completion(completion_id: int) -> Response:
    completion = program_completion_controller.find_by_id(completion_id)
    if completion:
        return make_response(jsonify(completion.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Program Completion not found"}), HTTPStatus.NOT_FOUND)

@program_completion_bp.put('/<int:completion_id>')
def update_program_completion(completion_id: int) -> Response:
    content = request.get_json()
    completion = ProgramCompletion.create_from_dto(content)
    program_completion_controller.update(completion_id, completion)
    return make_response("Program Completion updated", HTTPStatus.OK)

@program_completion_bp.delete('/<int:completion_id>')
def delete_program_completion(completion_id: int) -> Response:
    program_completion_controller.delete(completion_id)
    return make_response("Program Completion deleted", HTTPStatus.NO_CONTENT)