import React from 'react';
import {TextField, Grid, Box, Select, MenuItem, InputLabel, FormControl, Chip} from "@mui/material";
import './Filter.css';

export default function Filter(){
    const allOffers = ["Resume Review", "Mock Interview", "Career Advice", "Referral"];
    const [offer, setOffer] = React.useState([]);
    
    const allConcents = ["Front End", "Back End", "Database", "Researching", "AI/ML", "Infrastructure", "Business Analytics", "Cloud Solutions", "Automation", "Product Manager", "Testing"];
    const [concent, setConcent] = React.useState([]);

    const allJobs = ["Software Engineer", "Data Scientist", "AI/ML Engineer", "Product Manager", "Electrical Engineer"];
    const [job, setJob] = React.useState([]);

    const handleConcent = (event) => {
        const {
          target: { value },
        } = event;
        setConcent(
          // On autofill we get a stringified value.
          typeof value === 'string' ? value.split(',') : value,
        );
      };

    const handleOffer = (event) => {
        const {
          target: { value },
        } = event;
        setOffer(
          // On autofill we get a stringified value.
          typeof value === 'string' ? value.split(',') : value,
        );
      };

    const handleJob = (event) => {
        const {
          target: { value },
        } = event;
        setJob(
          // On autofill we get a stringified value.
          typeof value === 'string' ? value.split(',') : value,
        );
      };

    return (
        <div className="filter">
            <TextField className="TextField" id="outlined-basic" variant="outlined" fullWidth label="Search Name"/>
            <br/> <br/>
            <Grid container>
                <Grid item xs={5}>
                    <FormControl fullWidth>
                        <InputLabel id="offer">Offer</InputLabel>
                        <Select labelId="offer" id="offer" value={offer} label="Offer" onChange={handleOffer} renderValue={(selected) => (
                            <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
                            {selected.map((value) => (
                                <Chip key={value} label={value} />
                            ))}
                            </Box>
                        )} >
                            {allOffers.map((name) => (
                            <MenuItem
                            key={name}
                            value={name}>
                            {name}
                            </MenuItem>
                        ))}
                        </Select>
                    </FormControl>
                </Grid>
                <Grid item xs={2}></Grid>
                <Grid item xs={5}>
                    <FormControl fullWidth>
                        <InputLabel id="concentration">Concentration</InputLabel>
                        <Select labelId="concentration" multiple id="concentration" value={concent} label="Concentration" onChange={handleConcent} renderValue={(selected) => (
                            <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
                            {selected.map((value) => (
                                <Chip key={value} label={value} />
                            ))}
                            </Box>
                        )}>
                            {allConcents.map((name) => (
                            <MenuItem
                            key={name}
                            value={name}>
                            {name}
                            </MenuItem>
                        ))}
                        </Select>
                    </FormControl>
                </Grid>
            </Grid>
            <br/> <br/>
            <Grid container>
                <Grid item xs={5}>
                    <FormControl fullWidth>
                        <InputLabel id="job">Job</InputLabel>
                        <Select labelId="job" multiple id="job" value={job} label="job" onChange={handleJob} renderValue={(selected) => (
                            <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
                            {selected.map((value) => (
                                <Chip key={value} label={value} />
                            ))}
                            </Box>
                        )}>
                            {allJobs.map((name) => (
                            <MenuItem
                            key={name}
                            value={name}>
                            {name}
                            </MenuItem>
                        ))}
                        </Select>
                    </FormControl>
                </Grid>
                <Grid item xs={2}></Grid>
                <Grid item xs={5}>
                    <TextField className="company" id="outlined-basic" variant="outlined" fullWidth label="Company"/>
                </Grid>
            </Grid>
            <br/> <br/>
            <React.Fragment>
                <Box>Year of experience:</Box>
                <TextField
                    label="From"
                    type="number"
                /> 
                
                <TextField
                    label="To"
                    type="number"
                /> 
            </React.Fragment>
        </div>
    )
}