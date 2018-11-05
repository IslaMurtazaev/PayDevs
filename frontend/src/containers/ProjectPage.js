import { connect } from "react-redux";

import { projectActions } from "../actions/project";
import ProjectPage from "../components/ProjectPage";

export default connect(
  state => ({
    user: state.user,
    projects: state.projects
  }),
  dispatch => ({
    getAllProjects: () => {
      dispatch(projectActions.getAll());
    }
  })
)(ProjectPage);
