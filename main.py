from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema
import psycopg2

# from app.gql.mutation import Mutation
from app.gql.query import Query
# from app.db.database import session_maker, init_db

app = Flask(__name__)

schema = Schema(query=Query)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,
    )
)

@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    # with session_maker() as session:
    #     pass
    app.run(host="0.0.0.0", port=5000)


