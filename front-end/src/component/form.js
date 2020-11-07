import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Link from '@material-ui/core/Link';
import Typography from '@material-ui/core/Typography';
import { IconButton, List } from '@material-ui/core';
import { Autorenew } from '@material-ui/icons'
import Report from './report'
const axios = require('axios');

const useStyles = makeStyles({
  root: {
    width: 345,
  },
  media: {
    height: 140,
  },
  xs: {
    fontSize: 10,
  }
});

export default function Form() {
  const classes = useStyles();
  const [generated, setGenerated] = useState(false);
  const [generating, setGenerating] = useState(false);
  const [showReport, setShowReport] = useState(false);
  const [reportView, setReportView] = useState(null);
  const [result, setResult] = useState(null);

  const onClickGenerate = () => {
    setGenerating(true)
    axios.get("http://localhost:5000/generate")
      .then(res => {
        setGenerating(false);
        setReportView(<Report data={res.data.report}/>)
        setResult(res.data);
        setGenerated(true);
      })
      .catch(err => {
        console.log(err)
        setGenerating(false)
        setGenerating(false)
      });
  }
  const onClickReport = () => {
    setShowReport(!showReport);
  }
  return (
    <Card className={classes.root}>
      <CardActionArea>
        <CardMedia
          className={classes.media}
          image="/bg.png"
          title="Randomizer"
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="h2">
            Randomizer
          </Typography>
          <Typography variant="body2" color="textSecondary" component="p">
            {!showReport ?
              `is just a tool that help you to generate four (4) types of printable random objects and store them in a single file, each object will be separated by a ",". These are the 4 objects: alphabetical strings, real numbers, integers, alphanumerics.`
              : reportView}

          </Typography>
        </CardContent>
      </CardActionArea>
      <CardActions>
        <Button disabled={generating} onClick={onClickGenerate} size="small" color="primary" className={classes.xs} variant="outlined">{generated ? 'Regenerate' : generating?'Generating...':'Generate'}</Button>
        {generated?<Link href={result.file_url} color="secondary" className={classes.xs}>Download</Link>:''}
        <Button onClick={onClickReport} disabled={!generated} size="small" color="default" variant="outlined" className={classes.xs} style={{ marginLeft: 'auto' }}>
          {showReport?'Close Report':'Report'}
        </Button>

      </CardActions>
    </Card>
  );
}
