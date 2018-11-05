import { connect } from "react-redux";
import { projectActions } from "../actions/project";

import Project from "../components/Project";

const mapStateToProps = (state, ownProps) => ({
  project: state.project
    ? state.project
    : state.projects.find(project => project.id === +ownProps.match.params.id)
});

const mapDispatchToProps = (dispatch, ownProps) => ({
  removeProject: id => {
    dispatch(projectActions.remove(id));
  },
  getTotal: id => {
    dispatch(projectActions.getTotal(id));
  },
  getProject: () => {
    dispatch(projectActions.get(+ownProps.match.params.id));
  }
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Project);
