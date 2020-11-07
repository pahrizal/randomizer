import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import ListItemAvatar from '@material-ui/core/ListItemAvatar';
import Avatar from '@material-ui/core/Avatar';
import { Typography } from '@material-ui/core';

export default function Report({ data }) {
    return (
        <List>
            <ListItem>
                <ListItemAvatar>
                    <Avatar>
                        A
          </Avatar>
                </ListItemAvatar>
                <ListItemText primary="Alphabetical String" secondary={<Typography color="primary">{data[0]}</Typography>} />
            </ListItem>
            <ListItem>
                <ListItemAvatar>
                    <Avatar>
                        R
          </Avatar>
                </ListItemAvatar>
                <ListItemText primary="Real Number" secondary={<Typography color="primary">{data[1]}</Typography>} />
            </ListItem>
            <ListItem>
                <ListItemAvatar>
                    <Avatar>
                        I
          </Avatar>
                </ListItemAvatar>
                <ListItemText primary="Integer" secondary={<Typography color="primary">{data[2]}</Typography>} />
            </ListItem>
            <ListItem>
                <ListItemAvatar>
                    <Avatar>
                        Aln
          </Avatar>
                </ListItemAvatar>
                <ListItemText primary="Alphanumeric String" secondary={<Typography color="primary">{data[3]}</Typography>} />
            </ListItem>
        </List>
    );
}
