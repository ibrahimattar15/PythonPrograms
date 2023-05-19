from bs4 import BeautifulSoup
# with open('home.html','r') as fp:
#     content = fp.read()
#
#     soup = BeautifulSoup(content,'lxml')
#     #print(soup.prettify())
#     #tags = soup.find('h5')
#     # course_html_tags = soup.find_all('h5')
#     # for course in course_html_tags:
#     #     print(course.text)
#     course_cards = soup.find_all('div',class_='cards')
#     for course in course_cards:
#         course_name = course.h5
#         co = course_name.text
#         course_price = course.a
#         price = course_price.text.split()[-1]
#         print(f'{co} costs {price}')
#
#     #print(course_cards)
import time
import requests
print('Put some skills that you are not faliliar with')
undfamiliar_skills = input('>')
print(f'Filtering out {undfamiliar_skills}')
def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    # print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')
    # jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    # print(jobs)
    #job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
    #compnay_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
    #skills = job.find('span', class_='srp-skills').text.replace(' ', '')
    #publish_date = job.find('span', class_='sim-posted').span.text
    # print(publish_date)
    # print(skills)
    # print(compnay_name)
    # print(f"""
    # Compnay Name:{compnay_name}
    # Required Skills:{skills}
    # Publish Date:{publish_date}
    # """)
    #
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        publish_date = job.find('span', class_='sim-posted').span.text
        if 'few' in publish_date:
            compnay_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            job_link = job.header.h2.a['href']
            if undfamiliar_skills not in skills:
                with open(f'posts/{index}.txt','w') as fp:
                    fp.write(f'Company Name:{compnay_name.strip()} \n')
                    fp.write(f'Required Skills:{skills.strip()} \n')
                    fp.write(f'Publish Date:{publish_date} \n')
                    fp.write(f'More Info:{job_link} \n')
                print(f'file saved:{index}')
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} in minutes.....')
        time.sleep(time_wait*60)



