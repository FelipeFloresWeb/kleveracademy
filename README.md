


<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  

![kleverAcademyLogo](https://user-images.githubusercontent.com/78596051/176555372-5de3dd88-6cba-499e-bdc5-2d841f9a7060.png)


  <p align="center">
    <a href="https://klever-academy.netlify.app/">View Demo</a>
    ·
    <a href="https://github.com/FelipeFloresWeb/kleveracademy/issues">Report Bug</a>
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About The Project


Nowadays we come across many people who have "fear" or "aversion" to work with cryptocurrencies often this is due to lack of knowledge. For this reason, we thought of making a site where the user can study and learn about the subject and thus be able to enter this new world...


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#-docker-">Docker</a></li>
        <li><a href="#admin">Admin</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Next.js](https://nextjs.org/) (Front End: <a href="https://github.com/brunogcpinheiro/klever-academy"  target="_blank">Repository</a>)
* [Django](https://www.django-rest-framework.org/) (Back End: This repository)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

* [Python](https://www.python.org/downloads/)
* [Postgresql](https://www.postgresql.org/)
<p>You can also run this project through Docker</p>

* [Docker](https://www.docker.com/)

### Installation

1. Clone the repo
 ```sh
 git clone git@github.com:FelipeFloresWeb/kleveracademy.git
 ```

2. Access project folder
 ```sh
 cd kleveracademy
 ```

3. Create and activate the virtual development environment
 ```sh
 python -m venv venv.
 .\venv\Scripts\activate 
 ```

 4. Install the project's development dependencies
 ```sh
 pip install -r requirements.txt
 ```
 
 5. Create an '.env' file and add the necessary information for connecting to your Postgresql database:
 ```sh
 SECRET_KEY='(Your Choose)'
 NAME="For Connection DB"
 USER="For Connection DB"
 PASSWORD="For Connection DB"
 HOST=""
 PORT=""
 DEBUG=("TRUE" or "FALSE")
 ```
 
 6. Run migrations
 ```sh
 python .\manage.py migrate kleverApp
 ```
 
 6. Start the server
 ```sh
 python .\manage.py runserver
 ```
   
# ❗❗❗ DOCKER ❗❗❗
###  To run the application via Docker just run the commands inside 'commands.txt' ou run de command:
 ```sh
 docker compose up 
 ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ADMIN -->
## Admin
To access the application's administration system, simply access the '/admin' route.
To gain access to the system you need to create a super user with the following command:

 ```sh
py manage.py createsuperuser
 ```

<!-- ROADMAP -->
## Roadmap

User-Related Actions:
- [x] Create
- [x] Authentication
- [x] Log in
- [x] Log out

For Vídeos:
- [x] Catch all
- [x] Get by id
- [x] Add favorite
- [x] Remove from favorites
- [x] Grab all favorites
- [x] Rate

For Articles:
- [x] Catch all
- [x] Get by id

## :hourglass: Comming Soon :hourglass::
- [ ] Courses
- [ ] User Level
- [ ] User Points

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>
