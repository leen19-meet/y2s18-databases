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
	knowledge = session.query(Knowledge).filter_by(artName = article_title).first()
	knowledge.rating  = updated_rating 
	session.commit()

def edit_article_rating(threshold):
	pass

My_knowledge = Knowledge(artName= "music", topic="Music affecting the brain", rating= 9)
My_knowledge2 = Knowledge(artName= "chemistry", topic="It's all about chemistry", rating= 10)
My_knowledge3 = Knowledge(artName= "politics", topic="politics on a daily basis  ", rating= 9)


add_article("music", "Music affecting the brain", 9 )
edit_rating(7,"music")
print(query_all_articles())
(query_article_by_topic("The history of dancing"))
delete_article_by_topic("The history of dancing")
delete_all_articles()






