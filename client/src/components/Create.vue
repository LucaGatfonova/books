<template>
  <div class="container mt-4">
    <form @submit.prevent="insertBook">
      <input
      type="text"
      class="form-control"
      placeholder="Please enter your title"
      v-model="title"
      />
      <br/>
      <input
      type="text"
      class="form-control"
      placeholder="Please enter your author"
      v-model="author"
      />
      <br/>

      <textarea rows="10"
        class="form-control"
        placeholder="Please enter your text"
        v-model="text">
      </textarea>
      <br/>
      <div>
        <label>Read?</label>
        <input type="radio" :value="true" v-model="isRead"> yes
        <input type="radio" :value="false" v-model="isRead"> no
      </div>
      <button
        class="btn btn-success mt-4"
      >
        Add book
      </button>
    </form>
    <div v-if="error"
    class="alert alert-warning alert-dismissible fade show mt-5"
    role="alert"
    >
      <strong>{{error}}</strong>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      title: null,
      author: null,
      text: null,
      isRead: null,
      error: null,
    };
  },

  methods: {
    insertBook() {
      if (!this.title || !this.author || !this.text) {
        this.error = 'Please add all fields';
      } else
        fetch('http://127.0.0.1:5000/add', {
        method: 'POST',
        headers: {
          "Content-Type": 'application/json'
        },
        body: JSON.stringify({title:this.title, author:this.author, text:this.text, isRead:this.isRead}),
      })
      .then(resp => resp.json())
      .then(() => {
        this.$router.push({
          name:'Books'
        })
      })
      .catch(error => {
        console.log(error);
      })
    }
  },
};
</script>
