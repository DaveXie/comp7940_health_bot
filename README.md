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

![image](https://github.com/DaveXie/comp7940_health_bot/blob/main/resources/workflow.png)

Change committed and pushed to GitHub —> 

Build image through Dockerfile (GitHub Actions) —>

Push image to Azure Container Registry (GitHub Actions)—>

Deploy container to Azure Container Instances (GitHub Actions)

### Usage

- **/start:**

    ![image](https://github.com/DaveXie/comp7940_health_bot/blob/main/resources/start.png)

- **Send your weight record:**

    ![image](https://github.com/DaveXie/comp7940_health_bot/blob/main/resources/weight.png)

    *The bot can notice your weight gain/lost/no_change.*

- **Search food information:**

    ![image](https://github.com/DaveXie/comp7940_health_bot/blob/main/resources/food.png)

- **/help:**

    ![image](https://github.com/DaveXie/comp7940_health_bot/blob/main/resources/help.png)

- **Reply to error input:**

    ![image](https://github.com/DaveXie/comp7940_health_bot/blob/main/resources/error.png)
