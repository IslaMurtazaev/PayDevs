import React, { Component } from "react";
import { connect } from "react-redux";

import {hourPaymentActions} from '../../actions/hourPayment';
import HourPaymnetItem from './HourPaymentItem';




class HourPayments extends Component {
  onClick() {
    this.props.onGetAllProjects();
  }

  componentDidMount() {
    const { project } = this.props;
    this.props.onGetAllhourPayment(project.id);
  }

  render() {
    
    const { hourPayments} = this.props;
    console.log(hourPayments)
    const { project } = this.props;
    

    return (
      <div>
        <ul>
          {hourPayments.map(hourPaymnet=>(
            <li key={hourPaymnet.id}>
                <HourPaymnetItem hourPaymnet={hourPaymnet}  
                projectId={project.id} 
                onDelete={this.props.onDeletehourPayment}/>
            </li>)
          )
          }
        </ul>
          
      </div>
    );
  }
}

const mapStateToProps = (state) => {
    
    return {
      hourPayments: state.hourPayments
    };
  };

const mapDispatchToProps = (dispatch) => {
    return {
        onGetAllhourPayment: (projectId) => {
            dispatch(hourPaymentActions.getAll(projectId))
        },
        onDeletehourPayment: (hourId) => {
            dispatch(hourPaymentActions.deleteHour(hourId))
        }
    }
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(HourPayments);
