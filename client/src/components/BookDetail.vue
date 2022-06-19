<template>
  <div class="container mt-5">
      <h2>{{ books.title }}</h2>
      <h5>Author: {{ books.author }}</h5>
      <p class="mt-3">
        <b>Description:</b> {{ books.text }}
      </p>
      <p class="mt-3">
        <b>Read:</b>
         <span v-if="books.isRead">✅</span>
         <span v-else>❌</span>
      </p>

     <router-link
     :to="{name:'edit', params:{id:books.id}}"
     class="btn btn-warning btn-sm"
     >
     Update
     </router-link>

     <button
       class="btn btn-danger btn-sm"
       @click="deleteBooks"
     >
       Delete
     </button>
  </div>
</template>

<script>

export default {
  data() {
    return {
      books: {},
    };
  },
  props: {
    id: {
      type: [Number, String],
      required: true,
    },
  },

  methods: {
    deleteBooks() {
      fetch(`http://127.0.0.1:5000/delete/${this.id}/`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then(() => {
          this.$router.push({
            name: 'Books',
          });
        })
        .catch(error => {
          console.log(error);
        });
    },

    getBookDate() {
      fetch(`http://127.0.0.1:5000/get/${this.id}/`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then(resp => resp.json())
        .then(data => {
          this.books = data;
        })
        .catch(error => {
          console.log(error);
        });
    },
  },
  created() {
    this.getBookDate();
  },

};
</script>
