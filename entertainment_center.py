import fresh_tomatoes
import media

#stores movie information using Movie() class in media.py for each movie title


#toy_story = media.Movie("Toy Story",
 #                        "A story of a boy and his toys that come to life",
  #                       "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
   #                      "https://www.youtube.com/watch?v=vwyZH85NQC4")

#avatar = media.Movie("Avatar",
 #                    "A marine on an alien planet",
  #                   "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
   #                  "https://www.youtube.com/watch?v=5PSNL1qE6VY")


a300 = media.Movie("300",
                  "army of Spartan 300 soldiers to fight the large Persian army",
                  "http://images.moviefanatic.com/iu/v1394821056/300-movie-poster.jpg",
                   "https://www.youtube.com/watch?v=WorI5HPWbpg",
                   "Gerard Butler",
                   "2001")


before_sunset = media.Movie("Before Sunset",
                            "2 people meeting again after 9 years",
                            "http://images.fandango.com/r96.5/ImageRenderer/1040/650/redesign/areas/movie/moviesubpages/img/noimage_900x900.jpg/157491/images/masterrepository/fandango/157491/before%20sunset.jpg",
                            "https://www.youtube.com/watch?v=6a13q5tUGdg",
                            "Ethan Hawke, Julie Delpy",
                            "2007")
                            

batman_dark_knight = media.Movie("The Dark Knight",
                     "Batman faces the Joker",
                     "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX640_SY720_.jpg",
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                                 "Christian Bale",
                                 "2008")

gladiator = media.Movie("Gladiator",
                        "Roman General sold as a slave then become a gladiator",
                        "https://zuts.files.wordpress.com/2013/06/gladiator-2000-poster.jpg",
                        "https://www.youtube.com/watch?v=ol67qo3WhJk",
                        "Russel Crowe",
                        "2001")

forrest_gump = media.Movie("Forrest Gump",
                           "Forrest Gump, a simple person and his place in pop culture",
                           "http://2.bp.blogspot.com/-i03dWHqsKuY/Ucw2YpUKlOI/AAAAAAAAAFQ/NqfUh7pHZZQ/s1456/forrest-gump-poster-1994-tom-hanks.png",
                           "https://www.youtube.com/watch?v=eYSnxZKTZzU",
                           "Tom Hanks",
                           "1999")


midnight_in_paris = media.Movie("Midnight in Paris",
                                "A writer finding inspiration, discovers Paris being magical at midnight",
                                "http://www.impawards.com/2011/posters/midnight_in_paris_xlg.jpg",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4",
                                "Owen Wilson",
                                "2011")

fight_club = media.Movie("Fight Club",
                         "A person starts a club to vent frustrations",
                         "http://mtv.mtvnimages.com/shared/media/images/acovers/standard/dra200/a243/a24378zu88r.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg",
                         "Edward Norton, Brad Pitt",
                         "1999")

toy_story3 = media.Movie("Toy Story",
                         "Adventures of toys in search for a new owner",
                         "https://headinavice.files.wordpress.com/2013/03/toy-story-3-official-movie-poster1.jpg",
                         "https://www.youtube.com/watch?v=JcpWXaA2qeg",
                         "Tom Hanks",
                         "2010")

v_for_vendetta = media.Movie("V for Vendetta",
                             "A masked individual terrorizing a futuristing England",
                             "http://i822.photobucket.com/albums/zz143/TheLostArchive/v_for_vendetta_ver4_zps3a31f773.jpg",
                             "https://www.youtube.com/watch?v=lSA7mAHolAw",
                             "Natalie Portman, Hugo Weaving",
                             "2006")



#putting all the movies in a list
movies = [a300, before_sunset, batman_dark_knight, gladiator, forrest_gump, midnight_in_paris, fight_club, toy_story3, v_for_vendetta]


#using fresh_tomatoes to build a page displaying all the movies in the list
fresh_tomatoes.open_movies_page(movies)
