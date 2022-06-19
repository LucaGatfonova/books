<template>
 <nav class="navbar navbar-expand-lg bg-light">
  <div class="container">
    <router-link class="navbar-brand" to="/">Books</router-link>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item">
         <router-link
          to="/create">
          <button
            type="button"
            class="btn btn-success btn-sm"
          >
            Add Book
          </button>
         </router-link>
        </li>

      </ul>
    </div>
  </div>
 </nav>
</template>

<script>

export default {

};
</script>
