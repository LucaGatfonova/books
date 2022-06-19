<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Read?</th>
              <th scope="col">Description</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="book in books" :key="book.id">
              <td>{{ book.title }}</td>
              <td>{{ book.author }}</td>
              <td>
                <span v-if="book.isRead">✅</span>
                <span v-else>❌</span>
              </td>
              <td>
                <router-link
                :to="{name:'detail', params:{id:book.id}}"
                >
                Detailed description
                </router-link>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      books: [],
    };
  },

  methods: {
    getBooks() {
      fetch('http://127.0.0.1:5000/get', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then(resp => resp.json())
        .then(data => {
          this.books.push(...data);
        })
        .catch(error => {
          console.log(error);
        });
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
