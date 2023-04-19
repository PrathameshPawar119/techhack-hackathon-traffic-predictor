<template>
    <div class="SignupComponent">
        <v-text-field
            v-model="registerform.name"
            label="Name"
            placeholder="Enter your name"
            type="text"
            name="name"
            variant="outlined"
            required
            color="success"
            class="mx-4"
            :error-messages="v$.name.$errors[0] ? v$.name.$errors[0].$message : ''"
        ></v-text-field>
        <v-text-field
            v-model="registerform.password"
            label="Password"
            placeholder="Enter Password"
            type="password"
            name="password"
            variant="outlined"
            required
            color="success"
            class="mx-4"
            :error-messages="v$.password.$errors[0] ? v$.password.$errors[0].$message : ''"
        ></v-text-field>
        <v-text-field
            v-model="registerform.c_password"
            label="Confirm Password"
            placeholder="Confirm Password"
            type="password"
            name="c_password"
            variant="outlined"
            required
            color="success"
            class="mx-4"
            :error-messages="v$.c_password.$errors[0] ? v$.c_password.$errors[0].$message : ''"
        ></v-text-field>
        <v-text-field
            v-model="registerform.contact"
            label="Contact"
            placeholder="Enter Contact Number"
            type="number"
            name="contact"
            hide-spin-buttons
            variant="outlined"
            color="success"
            class="mx-4"
            :error-messages="v$.contact.$errors[0] ? v$.contact.$errors[0].$message : ''"
        ></v-text-field>

        <div class="d-flex justify-center">
            <v-btn color="primary" class="p-2 ma-2 mb-4" @click.prevent="registerData">Sign up</v-btn>
        </div>
    </div>
</template>

<script setup>
import { reactive } from 'vue';
import { useVuelidate } from "@vuelidate/core";
import { required, helpers, minLength, integer } from "@vuelidate/validators";

const props = defineProps({
    formData: {
        type: Object,
        required: true
    }
})

const { $useFetchApi: useFetchApi } = useNuxtApp();

const requiredNameLength = ref(3);
const contactlength = ref(10);

const registerform = reactive({
    name: null,
    password: null,
    c_password: null,
    contact: null
});

const rules = computed(() => {
  const localRules = {
    name: {
      required: helpers.withMessage("Name is required", required),
      minLength: minLength(requiredNameLength.value),
    },
    password: {
      required: helpers.withMessage("Password is required", required),
      minLength: minLength(requiredNameLength.value),
    },
    c_password: {
      required: helpers.withMessage("Password is required", required),
      minLength: minLength(requiredNameLength.value),
    },
    contact: {
      integer: helpers.withMessage(`must be a valid contact`, integer),
      minLength: minLength(contactlength.value),
    },
  };

  return localRules;
});

const v$ = useVuelidate(rules, registerform, {$lazy:true})

async function registerData(){
    const formvalid = await v$.value.$validate()

    if(formvalid){
        const { pending, data, error, refresh } = await useFetchApi("auth/register", {
            method: "POST",
            body: {
                email: props.formData.email,
                name: registerform.name,
                password: registerform.password,
                c_password: registerform.c_password,
                contact: registerform.contact,
            },
        });

        if(data.value){
            console.log("Registered Successfully");
            await navigateTo('/');
        }else if(error.value){
            console.log("Register errorr");
        }
    }
}

</script>