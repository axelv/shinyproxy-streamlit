## How to setup the ShinyProxy/Streamlit app
1. Clone the [repository containing the Dockerfile]():
  ```bash
  git clone 
  ```
2. `cd` to the repo directory and build the docker container:
  ```bash
  docker build -t shinyproxy-streamlit .
  ```
  
3. Run Shiny Proxy with the configuration specified in `application.yml`
 
