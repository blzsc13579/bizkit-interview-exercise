from flask import Blueprint, request, jsonify

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    search = []

    # The user can also pass just the id as a parameter and 
    # it should just return the user with that id
    if (args.get("id") is not None and args.get("name") is None and args.get("age") is None and args.get("occupation" is None)):
        for user in USERS:
            if (str(user["id"]) == args.get("id")):
                search.append(user)
                jsonify(search)
        return search

    
    # The user can also pass multiple parameters and 
    # the function should return all the users that match ANY of the parameters provided.
    min_age = int(args.get("age", 0)) - 1
    max_age = int(args.get("age", 0)) + 1
    for user in USERS:
        search_age = user["age"]
        if ( args.get("id") is not None 
                and args.get("id") == user["id"]
            or (args.get("name") is not None 
                and args.get("name").lower() in user["name"].lower())
            or (args.get("occupation") is not None 
                and args.get("occupation").lower() in user["occupation"].lower())
            or (min_age<=search_age<=max_age)
            ):
            search.append(user)

        jsonify(search)
    return  search
