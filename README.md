## How to setup the ShinyProxy/Streamlit app
1. Clone this [repository](https://github.com/Tiro-health/shiny-proxy-helloworld):
  ```bash
  git clone git@github.com:Tiro-health/shiny-proxy-helloworld.git
  ```
2. `cd` to the folder containing the [Dockerfile](Dockerfile) and build the docker container:
  ```bash
  docker build -t shinyproxy-streamlit .
  ```
  
3. Run Shiny Proxy with the configuration specified in [application.yml](application.yml)
 
