<template lang="html">
  <div class="container">
    <div class="login">
      <div>
        <h1>Welcome to Tweetbook!</h1>
        <h3>Please login</h3>
      </div>
      <form class="form">
        <div class="field">
          <i class="fa fa-user" aria-hidden="true"></i>
          <input
            v-model="username"
            type="text"
            placeholder="Username"
            autofocus="autofocus"
            maxlength="150"
            id="id_username">
        </div>
        <div class="field">
          <i class="fa fa-lock" aria-hidden="true"></i>
          <input
            v-model="password"
            type="password"
            placeholder="Password"
            id="id_password">
        </div>
        <button
          @click.prevent="authenticate"
          class="button primary"
          type="submit">
          Log In
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import jwtDecode from 'jwt-decode';

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    authenticate() {
      const payload = {
        screen_name: this.username,
        password: this.password,
      };
      axios.post(this.$store.state.endpoints.obtainJWT, payload)
        .then((response) => {
          this.$store.commit('updateToken', response.data.access);
          // get and set auth user
          const base = {
            baseURL: this.$store.state.endpoints.baseUrl,
            headers: {
            // Set your Authorization to 'JWT', not Bearer!!!
              Authorization: `JWT ${this.$store.state.jwt}`,
              'Content-Type': 'application/json',
            },
            xhrFields: {
              withCredentials: true,
            },
          };
          // Even though the authentication returned a user object that can be
          // decoded, we fetch it again. This way we aren't super dependant on
          // JWT and can plug in something else.
          const userId = jwtDecode(this.$store.state.jwt).user_id;
          console.log(userId);
          const axiosInstance = axios.create(base);
          axiosInstance({
            url: `/users/${userId}`,
            method: 'get',
            params: {},
          })
            .then((res) => {
              this.$store.commit('setAuthUser', { authUser: res.data, isAuthenticated: true });
              this.$router.push({ name: 'Layout' });
            });
        })
        .catch((error) => {
          console.log(error);
          console.debug(error);
          console.dir(error);
        });
    },
  },
};
</script>

<style lang="css">
.container {
  display: flex;
  height: 100vh;
}
.login {
  display: flex;
  flex-direction: column;
  max-width: 380px;
  width: 75%;
  margin: auto;
  /* align-items: center; */
  /* justify-content: center; */
}
input {
  outline: none;
  border: none;
  padding: 0 15px;
  font-size: 16px;
  background-color: transparent;
}
.field {
  padding: 10px 15px;
  border-radius: 9999px;
  background-color: white;
  margin-bottom: 15px;
  font-size: 16px;
}
button {
  border: none;
  padding: 10px 15px;
  background-color: rgb(85, 168, 250);
  border-radius: 20px;
  color: white;
  font-size: 14px;
  font-weight: 700;
  transition: 0.1s;
  width: 100%;
}
button:hover {
  background-color: rgb(23, 136, 250);
}
h1, h3 {
  text-align: center;
}
</style>
