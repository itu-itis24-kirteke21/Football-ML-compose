# Football Match Winner – Docker Compose Demo
 Two services:- **trainer**: trains a multinomial logistic regression and writes a model into 
`/shared/model`.- **api**: Flask service serving `/predict` and logging predictions to SQLite 
in `/shared/predictions.db`.
 ## Run
 ```bash
 docker compose up --buil