import axios from "axios"
export const state = () => ({
    token: null,
    is_staff: false
})

export const actions = {
    auth(context, token) {
        context.commit('setToken', token)
        context.commit('setStaff')
    }
}


export const mutations = {
    setToken(state, token) {
        state.token = token
    },
    setStaff(state) {
        axios.get("http://127.0.0.1:8000/auth/users/me/", { headers: { 'Authorization': `Token ${state.token}` } }).then((resp) => {
            console.log(resp)
        })
    }
}