# comp7940 healthchat bot

**This project is for COMP7940 Cloud Computing.**

**Produced by Zhicheng Xie & Bingxiang He.**

### Components

**This project covers the following components:**

- A Telegram Chat Bot
    - t.me/lets_healthbot
- A module to adopt the weight recording feature.
    - with RedisLabs
- A module to adopt calories calculating feature.
    - with rapidapi.com/calorieninjas/api/calorieninjas
- A Cloud platform to deploy the codes.
    - with Azure Container Registry & Container Instances
- Docker container technologies.

### How it Works?

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1435b726-97ac-4fb3-9e04-d2f06dfbed02/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1435b726-97ac-4fb3-9e04-d2f06dfbed02/Untitled.png)

Change committed and pushed to GitHub —> 

Build image through Dockerfile (GitHub Actions) —>

Push image to Azure Container Registry (GitHub Actions)—>

Deploy container to Azure Container Instances (GitHub Actions)

### Usage

- **/start:**

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4b02e194-3246-4b76-968e-24447178e30c/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4b02e194-3246-4b76-968e-24447178e30c/Untitled.png)

- **Send your weight record:**

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b697b038-a642-45ac-9622-455e0f2864e2/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b697b038-a642-45ac-9622-455e0f2864e2/Untitled.png)

    *The bot can notice your weight gain/lost/no_change.*

- **Search food information:**

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cc565c4a-1cb7-4143-a189-4b588dde3c8b/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cc565c4a-1cb7-4143-a189-4b588dde3c8b/Untitled.png)

- **/help:**

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/198fa321-1ea3-4286-b64d-7a9efcb986b2/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/198fa321-1ea3-4286-b64d-7a9efcb986b2/Untitled.png)

- **Reply to error input:**

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4766fc31-a2f2-4e86-a77f-730e83564cee/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4766fc31-a2f2-4e86-a77f-730e83564cee/Untitled.png)
