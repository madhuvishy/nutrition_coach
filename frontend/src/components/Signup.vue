<template>
    <div class='signup'>
        <logged-out-header></logged-out-header>
        <h1>Sign-up Form</h1>
        <form id="signup" v-on:submit.prevent="signupUser" >
            <input v-model="username" type="text" placeholder="Enter Username" required>
            <input v-model="password" type="password" placeholder="Enter Password" required>
            <button type="submit">Submit</button>
        </form>
    </div>
</template>


<script>
/* eslint-disable */
    import auth from '@/auth.js'
    import LoggedOutHeader from '@/components/LoggedOutHeader'
    export default {
        name: 'signup',
        data: function() {
            return {
                username: '',
                password: '',
            }
        },
        components: {
          LoggedOutHeader
        },
        methods: {
            signupUser: function(evt) {
                auth.createUser(this.username, this.password, (token) => {
                    this.$emit('loginsuccess', token);
                    this.$router.push('Dashboard')
                });
            }
        }
    }
</script>
