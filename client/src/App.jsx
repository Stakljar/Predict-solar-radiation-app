import { BrowserRouter, Routes, Route } from "react-router-dom";
import GetStarted from "./routes/GetStarted";
import Shared from "./routes/Shared";
import Prediction from "./routes/Prediction"
import GraphPrediction from "./routes/GraphPrediction";
import NotFound from "./routes/NotFound";
import "./styles/App.css";

let singlePredictionRoute = "/single_prediction"
let graphPredictionRoute = "/graph_prediction"

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={ <Shared /> }>
            <Route index element={ <GetStarted /> }/>
            <Route path={ singlePredictionRoute } element={ <Prediction /> }/>
            <Route path={ graphPredictionRoute } element={ <GraphPrediction /> }/>
          </Route>
          <Route path="*" element={ <NotFound /> }/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App
export { singlePredictionRoute, graphPredictionRoute }
