import { connect } from "react-redux";

import { tasklyActions } from "../../actions/task";
import TasksScreen from "./TasksScreen";

const mapStateToProps = state => {
  return {
    tasks: state.tasks
  };
};

const mapDispatchToProps = dispatch => {
  return {
    getAllTasks: projectId => {
      dispatch(tasklyActions.getAll(projectId));
    },
    removeTask: taskId => {
      dispatch(tasklyActions.remove(taskId));
    }
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(TasksScreen);
