# kody_api

## Routes

---

### User

    GET /user - { "id": int }

    POST /user/create - { "id": int }

### Question

    GET /question/random

    POST /question/add - { question data }
    POST /question/add/multiple - [{ question data },]

### Profile

    GET /profile - { "id": int }

    POST /profile/create - { profile data }
