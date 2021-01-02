<template>
<div class="container">
  <h1 class="title">Task Manager</h1>
  <div class="columns">
    <div class="column is-4" v-for="status in taskStatuses">
      <p class="status has-background-primary has-text-white-ter mb-4">{{ status.toUpperCase() }}</p>
      <div class="board">
        <div v-for="task in tasks" v-bind:key="task.id">
          <div class="card" v-if="task.status === status">
            <header class="card-header">
              <p class="card-header-title">
                {{ task.title }}
              </p>
            </header>
            <div class="card-content">
              <p>{{ task.description }}</p>
              <p>{{ task.status }}</p>
            </div>
            <footer class="card-footer">
              <a href="#" class="card-footer-item" v-if="status != 'todo'">To Do</a>
              <a href="#" class="card-footer-item" v-if="status != 'in progress'">In Progress</a>
              <a href="#" class="card-footer-item" v-if="status != 'done'">Done</a>
            </footer>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000/api/'

export default {
  name: 'Home',
  data() {
    return {
      tasks: [],
      taskStatuses: ['todo', 'in progress', 'done']
    }
  },
  mounted() {
    this.getTasks()
  },
  methods: {
    getTasks() {
      axios({
        method: 'get',
        url: API_URL + 'tasks/',
        auth: {
          username: 'admin',
          password: 'password'
        }
      }).then(response => this.tasks = response.data)
    }
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Roboto&display=swap');

body {
    font-family: 'Roboto', Helvetica, sans-serif;
}

.select,
select {
    width: 100%;
}

.card {
    margin-bottom: 20px;
}

.status {
    line-height: 2em;
    text-align: center;
    box-shadow: 0 2px 2px 0 rgba(10, 10, 10, 0.2);
    font-family: 'Oswald', Helvetica, sans-serif;
    font-weight: 700;
    font-size: 1.5em;
}
</style>
