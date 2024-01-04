from . import mail, session

mail.Base.metadata.create_all(bind=session.engine)
