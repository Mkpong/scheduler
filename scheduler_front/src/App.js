import React from "react";
import { useState , useEffect } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import Table from 'react-bootstrap/Table'
import { Container } from "react-bootstrap";

function App() {

  const [data , setData] = useState({
    year: 2023,
    month : 9,
    day : 30,
    start : "Fri"
  })

  const [day , setDay] = useState([])

  const left_month = (e) => {
    if(data.month === 1){
      setData({
        ...data,
        year : data.year-1,
        month : 12
      })
    }
    else{
      setData({
        ...data,
        month : data.month-1
      })
    }
  }

  const right_month = (e) => {
    if(data.month === 12){
      setData({
        ...data,
        year : data.year+1,
        month : 1
      })
    }
    else{
      setData({
        ...data,
        month : data.month + 1
      })
    }
  }

  const get_day = () => {
    
  }

  useEffect = () => {

  }

  return (
    <div>
      <Container style={{height : "300px" , width: "200px", marginTop: "20px" , textAlign: "center"}}>
      <Table striped bordered hover>
        <thead>
        <tr>
          <th><button onClick={left_month}>{"<"}</button></th>
          <th colSpan = {5}>{data.year}.{data.month}</th>
          <th><button onClick={right_month}>{">"}</button></th>  
        </tr>
        <tr>
          <th>Mon</th>
          <th>Tue</th>
          <th>Wed</th>
          <th>Thu</th>
          <th>Fri</th>
          <th>Sat</th>
          <th>Sun</th>
        </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>2</td>
            <td>3</td>
            <td>4</td>
            <td>5</td>
            <td>6</td>
            <td>7</td>
          </tr>
          <tr>
            <td>8</td>
            <td>9</td>
            <td>10</td>
            <td>11</td>
            <td>12</td>
            <td>13</td>
            <td>14</td>
          </tr>
          <tr>
            <td>15</td>
            <td>16</td>
            <td>17</td>
            <td>18</td>
            <td>19</td>
            <td>20</td>
            <td>21</td>
          </tr>
          <tr>
            <td>22</td>
            <td>23</td>
            <td>24</td>
            <td>25</td>
            <td>26</td>
            <td>27</td>
            <td>28</td>
          </tr>
          <tr>
            <td>29</td>
            <td>30</td>
            <td>31</td>
          </tr>
        </tbody>
      </Table>
      </Container>
    </div>
  );
}

export default App;
