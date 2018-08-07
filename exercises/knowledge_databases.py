from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(artName, topic, rating):
	My_knowledge = Knowledge(
		artName = artName,
		topic = topic,
		rating = rating)
	session.add(My_knowledge)
	session.commit()
	


def query_all_articles():
	knowledge = session.query(
		Knowledge).all()
	return knowledge 
	

def query_article_by_topic(their_topic):
	knowledge  = session.query(
		Knowledge).filter_by(
			topic = their_topic).all()
	return knowledge 
	
#def query_article_by_rating(threshold):



def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(
		topic = topic).delete()
	session.commit() 
	

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

def edit_rating(updated_rating, article_title):
	knowledge = session.query(Knowledge).filter_by(article_name = article_title).first()
	knowledge.rating  = updated_rating 
	session.commit()




def edit_article_rating():
	pass


Name  | Year
Subhi | 2001
Ahmad | 1991