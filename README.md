# Flask_SQLAlchemy_tut

> This app is for trial of Flask_SQLAlchemy using flask-sqlalchemy documentation.

# What to Remember [used from https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/]
 > For the most part, you should use SQLAlchemy as usual. The SQLAlchemy extension instance creates, configures, and gives access to the following things:

SQLAlchemy.Model declarative model base class. It sets the table name automatically instead of needing __tablename__.

SQLAlchemy.session is a session that is scoped to the current Flask application context. It is cleaned up after every request.

SQLAlchemy.metadata and SQLAlchemy.metadatas gives access to each metadata defined in the config.

SQLAlchemy.engine and SQLAlchemy.engines gives access to each engine defined in the config.

SQLAlchemy.create_all() creates all tables.

You must be in an active Flask application context to execute queries and to access the session and engine.