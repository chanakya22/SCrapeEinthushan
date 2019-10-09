import requests
from bs4 import BeautifulSoup
import smtplib

# class Langugage:
#     Telugu="telugu"
#     Hindi="hindi"
#     Tamil="tamil"
#     Malayalam="malayalam"

# class GetMovies:

# def function(self):
#     print("constructor class")

# def scrape(self):
# raw_html = urllib.request.urlopen('https://einthusan.tv/movie/results/?find=Recent&lang=telugu')

counter=0
language=''
titles=''

while(counter < 4): 
    # print(counter)   
    if counter == 0 :
        language='telugu'
    elif counter == 1:
        language='hindi'
    elif counter == 2:
        language ='tamil'
    elif counter == 3:
        # print("in")
        language = 'malayalam'
    
    titles=titles+'****************************'+language+'****************************'+'\n'


    raw_html=requests.get('https://einthusan.tv/movie/results/?find=Recent&lang='+language).content
    # raw_html = open('https://einthusan.tv/movie/results/?find=Recent&lang=telugu').read()
    # soup = BeautifulSoup(raw_html, 'html.parser')
    soup=BeautifulSoup(raw_html,'lxml')


    for s in soup.select('section'):
        if s['id'] =='PGMovieResulter':
            for s_inner in s.select('section'):
                if s_inner['id'] == 'content' :
                    for s_inner_inner in s_inner.select('section'):
                        if s_inner_inner['id'] == 'UIMovieSummary':
                            for ul in s_inner_inner.select('ul'):
                                for li in ul.select('li'):
                                    for div in li.select('div'):
                                        for a in div.select('h3'):
                                            titles=titles+str(a.text)+" -------------------------> https://www.imdb.com/find?ref_=nv_sr_fn&q="+str(a.text)+"&s=tt\n"
                                            break
    counter=counter+1                                                                

print(titles)


s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication https://myaccount.google.com/lesssecureapps
s.login("id", "password") 
  
# message to be sent 
message = "Hola, \n Below is the list of new Einthushan Movies \n \n"+titles
  
# sending the mail 
s.sendmail("emailid@gmail.com", message) 
  
# terminating the session 
s.quit() 

# if __name__ == "__main__":

#     movies=GetMovies()
#     movies.scrape()

# def FetchIMDBRating(str movieName):
#     str n=''

