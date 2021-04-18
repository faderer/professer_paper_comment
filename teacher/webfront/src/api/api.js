// appfront/src/api/api.js
import axiosInstance from './index'

const axios = axiosInstance

export const getPapers = () => {return axios.get(`http://localhost:8000/api/paper/`)}

export const postPapers = (title, citation, date) => {return axios.post(`http://localhost:8000/api/paper/`, {'title': title, 'citation': citation,'pub_date':date})}

export const getComments = () => {return axios.get(`http://localhost:8000/api/comment/`)}

export const postComments = (teacher, content, pub_date) => {return axios.post(`http://localhost:8000/api/comment/`, {'teacher': teacher, 'content': content,'pub_date':pub_date})}

export const getUsers = () => {return axios.get(`http://localhost:8000/api/login/`)}

export const postUsers = (username, password, email) => {return axios.post(`http://localhost:8000/api/login/`, {'username': username, 'password': password,'email':email})}