from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import visitors_controller
from my_project.auth.domain.orders.Visitor import Visitor

visitor_bp = Blueprint('visitor', __name__, url_prefix='/visitor')

@visitor_bp.get('')
def get_all_visitors() -> Response:
    visitors = visitors_controller.find_all()
    visitors_dto = [visitor.put_into_dto() for visitor in visitors]
    return make_response(jsonify(visitors_dto), HTTPStatus.OK)

@visitor_bp.post('')
def create_visitor() -> Response:
    content = request.get_json()
    visitor = Visitor.create_from_dto(content)
    visitors_controller.create(visitor)
    return make_response(jsonify(visitor.put_into_dto()), HTTPStatus.CREATED)

@visitor_bp.get('/<int:visitor_id>')
def get_visitor(visitor_id: int) -> Response:
    visitor = visitors_controller.find_by_id(visitor_id)
    if visitor:
        return make_response(jsonify(visitor.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Visitor not found"}), HTTPStatus.NOT_FOUND)

@visitor_bp.put('/<int:visitor_id>')
def update_visitor(visitor_id: int) -> Response:
    content = request.get_json()
    visitor = Visitor.create_from_dto(content)
    visitors_controller.update(visitor_id, visitor)
    return make_response("Visitor updated", HTTPStatus.OK)

@visitor_bp.delete('/<int:visitor_id>')
def delete_visitor(visitor_id: int) -> Response:
    visitors_controller.delete(visitor_id)
    return make_response("Visitor deleted", HTTPStatus.NO_CONTENT)