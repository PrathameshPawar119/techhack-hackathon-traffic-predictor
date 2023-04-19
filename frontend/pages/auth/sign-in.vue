<template>
    <v-container fluid>
        <v-row justify="center" class="pa-2">
            <v-col cols="12" sm="8" md="6" lg="4" class="rounded-xl pa-4 mt-10 text-center">
                <v-card class="mx-auto rounded-xl" elevation="4" variant="outlined">
                    <div class="ma-4 rounded-xl py-3">
                        <v-card-title>
                            <h1 class="ma-3" style="font-size:54px">Shramik</h1>
                        </v-card-title>
                        <v-card-subtitle>
                            <h2 class="text-body-1 mb-3">We make your work done, sign-in!</h2>
                        </v-card-subtitle>
                         <v-btn-toggle
                            v-model="formData.method"
                            background-color="transparent"
                            class="ma-4"
                            variant="outlined"
                            mandatory
                            >
                            <v-btn icon value="email">
                                <v-icon icon="$email"></v-icon>
                            </v-btn>
                            <v-btn icon value="contact">
                                <v-icon icon="$phone"></v-icon>
                            </v-btn>
                        </v-btn-toggle>
                        <div v-if="formData.method=='email'">
                            <v-text-field
                                v-model="formData.identifier"
                                label="Email"
                                placeholder="Email"
                                type="email"
                                name="email"
                                required
                                variant="outlined"
                            >
                            </v-text-field>
                        </div>
                        <div v-if="formData.method=='contact'">
                            <v-text-field
                                v-model="formData.identifier"
                                label="Contact"
                                placeholder="Contact"
                                type="number"
                                name="contact"
                                required
                                variant="outlined"
                            >
                            </v-text-field>
                        </div>
                            <v-text-field
                                v-model="formData.password"
                                type="password"
                                label="Password"
                                name="password"
                                class="mt-2"
                                variant="outlined"
                                required
                            ></v-text-field>
                    </div>
                    <div class="d-flex justify-center">
                    <div v-if="pending">
                        <Loading message="Logging in"/>
                    </div>
                    <div v-else>
                        <v-btn
                            color="primary"
                            class="p-2 mb-3"
                            @click.prevent="loginWithIdentifier"
                            >Sign in</v-btn
                        >
                    </div>
                    </div>
                    <v-row class="my-4" justify="space-around">
                        <v-btn
                            variant="text"
                            size="small"
                            :to="{ path: '/auth/sign-up' }"
                            >Create an account</v-btn
                        >
                        <v-btn
                            variant="text"
                            size="small"
                            :to="{ path: '/auth/reset' }"
                            >Forgot password</v-btn
                        >
                    </v-row>
                </v-card>
            </v-col>
        </v-row>
    </v-container>

</template>

<script setup>
import { useVuelidate } from "@vuelidate/core";
import { required, email, helpers, minLength, integer } from "@vuelidate/validators";
import { reactive } from 'vue';
const {$sanctumAuth} = useNuxtApp();

definePageMeta({
    middleware: ["guest"]
})

useHead({
    title: "SignIn"
})
const formData = reactive({
    method: "email",
    identifier: null,
    password: null
})

const requiredNameLength = ref(3);
const rules = computed(() => {
  const localRules = {
    identifier: {},
    password: {
      required: helpers.withMessage("Password is required", required),
      minLength: minLength(requiredNameLength.value),
    },
  };
  if (formData.method == "email") {
    localRules.identifier = {
      required: helpers.withMessage("email is required", required),
      email: helpers.withMessage(`must be a valid email`, email),
    };
  }

  if (formData.method == "contact") {
    localRules.identifier = {
      required: helpers.withMessage("contact is required", required),
      integer: helpers.withMessage(`must be a valid contact`, integer),
    };
  }

  return localRules;
});

const v$ = useVuelidate(rules, formData, {$lazy:true})
async function loginWithIdentifier(){
    const formvalid = v$.value.$validate()
    if(formvalid){
        await $sanctumAuth.login(formData)
        .then((res) => {
            console.log(res);
        }).catch((error) => {
            console.log(error);
        })
    }
    else{
        console.log("Login error Formvalid", formvalid);
    }
}
</script>
