from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
	__tablename__ = 'knowledge'
	id = Column(Integer, primary_key=True)
	artName = Column(String)
	topic = Column(String)
	rating = Column(Integer)

	def __repr__(self):
		return("Id: {}\n"
				"Article name:{}\n"
				"Topic:{}\n"
				"Rating:{}\n".format(
					self.id, self.artName, self.topic, self.rating)
				

My_knowledge = Knowledge(artName= "music", topic="Music affecting the brain", rating= 9)
My_knowledge2 = Knowledge(artName= "chemistry", topic="It's all about chemistry", rating= 10)
My_knowledge3 = Knowledge(artName= "politics", topic="politics on a daily basis  ", rating= 9)

	